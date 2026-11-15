import Foundation
import PDFKit
import Vision
import AppKit
let args=CommandLine.arguments
guard let pdf=PDFDocument(url:URL(fileURLWithPath:args[1])) else {fatalError("PDF unavailable")}
for i in args.dropFirst(3).compactMap({Int($0)}) {
 autoreleasepool {
  guard let page=pdf.page(at:i-1) else{return}
  let im=page.thumbnail(of:NSSize(width:2300,height:3200),for:.mediaBox)
  var rect=CGRect(origin:.zero,size:im.size)
  guard let cg=im.cgImage(forProposedRect:&rect,context:nil,hints:nil) else{return}
  let req=VNRecognizeTextRequest()
  req.recognitionLevel = .accurate
  req.recognitionLanguages=["en-US"]
  req.usesLanguageCorrection=false
  do {
   try VNImageRequestHandler(cgImage:cg,options:[:]).perform([req])
   let text=(req.results ?? []).compactMap{$0.topCandidates(1).first?.string}.joined(separator:"\n")
   try text.write(toFile:"\(args[2])/\(i).txt",atomically:true,encoding:.utf8)
   print("PAGE \(i) \(text.count)")
  } catch {print("ERROR \(i) \(error)")}
 }
}
