import Foundation
import PDFKit
import Vision
import AppKit
let args=CommandLine.arguments
let path=args[1]
let out=args[2]
guard let pdf=PDFDocument(url:URL(fileURLWithPath:path)) else { fatalError("PDF unavailable") }
for i in args.dropFirst(3).compactMap({Int($0)}) {
 autoreleasepool {
  guard let page=pdf.page(at:i-1) else{return}
  let im=page.thumbnail(of:NSSize(width:1600,height:2300),for:.mediaBox)
  var rect=CGRect(origin:.zero,size:im.size)
  guard let cg=im.cgImage(forProposedRect:&rect,context:nil,hints:nil) else{return}
  let req=VNRecognizeTextRequest()
  req.recognitionLevel = .accurate
  req.recognitionLanguages=["en-US","ja-JP"]
  req.usesLanguageCorrection=true
  do {
   try VNImageRequestHandler(cgImage:cg,options:[:]).perform([req])
   let text=(req.results ?? []).compactMap{$0.topCandidates(1).first?.string}.joined(separator:"\n")
   try text.write(toFile:"\(out)/\(i).txt",atomically:true,encoding:.utf8)
   print("PAGE \(i) \(text.count) characters")
  } catch {print("ERROR \(i) \(error)")}
 }
}
