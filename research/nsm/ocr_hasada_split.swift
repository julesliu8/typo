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
  let im=page.thumbnail(of:NSSize(width:3000,height:4300),for:.mediaBox)
  var rect=CGRect(origin:.zero,size:im.size)
  guard let cg=im.cgImage(forProposedRect:&rect,context:nil,hints:nil) else{return}
  let req=VNRecognizeTextRequest()
  req.recognitionLevel = .accurate
  req.recognitionLanguages=["en-US","ja-JP"]
  req.usesLanguageCorrection=true
  do {
   var pieces:[String]=[]
   for side in 0...1 {
    let crop=CGRect(x:side*cg.width/2,y:0,width:cg.width/2,height:cg.height)
    guard let half=cg.cropping(to:crop) else{continue}
    try VNImageRequestHandler(cgImage:half,options:[:]).perform([req])
    pieces.append((req.results ?? []).compactMap{$0.topCandidates(1).first?.string}.joined(separator:"\n"))
   }
   let text=pieces.joined(separator:"\n\n[RIGHT SCANNED PAGE]\n\n")
   try text.write(toFile:"\(out)/\(i).txt",atomically:true,encoding:.utf8)
   print("PAGE \(i) \(text.count) characters")
  } catch {print("ERROR \(i) \(error)")}
 }
}
