import Foundation
import PDFKit
import AppKit
let args = CommandLine.arguments
let path = args[1]
let prefix = args[2]
guard let pdf = PDFDocument(url: URL(fileURLWithPath: path)) else { fatalError("PDF unavailable") }
for n in args.dropFirst(3).compactMap({Int($0)}) {
    guard let page = pdf.page(at: n-1) else { continue }
    let im = page.thumbnail(of: NSSize(width: 1800, height: 2500), for: .mediaBox)
    guard let tiff = im.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiff),
          let png = bitmap.representation(using: .png, properties: [:]) else { continue }
    try png.write(to: URL(fileURLWithPath: "\(prefix)_\(n).png"))
    print("rendered \(n)")
}
