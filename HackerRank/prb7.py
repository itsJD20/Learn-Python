def designerPdfViewer(h, word):
    m =0
    for i in word:
        v = ord(i)-ord("a")
        if m < h[v]:
            m = h[v]
    
    return len(word)*m