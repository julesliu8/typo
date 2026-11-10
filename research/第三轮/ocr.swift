import Foundation
import PDFKit
import Vision
let document = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1]))!
let start = CommandLine.arguments.count > 2 ? Int(CommandLine.arguments[2])! - 1 : 0
let end = CommandLine.arguments.count > 3 ? Int(CommandLine.arguments[3])! : document.pageCount
for n in start..<end {
 let page = document.page(at:n)!
 let rect = page.bounds(for:.mediaBox)
 let image = page.thumbnail(of:NSSize(width:rect.width*2,height:rect.height*2),for:.mediaBox)
 var r=CGRect(origin:.zero,size:image.size)
 guard let cg=image.cgImage(forProposedRect:&r,context:nil,hints:nil) else {continue}
 let req=VNRecognizeTextRequest();req.recognitionLevel = .accurate;req.usesLanguageCorrection = false
 try VNImageRequestHandler(cgImage:cg).perform([req])
 print("\n[PDF PAGE \(n+1)]\n")
 for x in req.results ?? [] {print(x.topCandidates(1).first!.string)}
}
