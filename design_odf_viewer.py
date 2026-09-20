def designerPdfViewer(h, word):
    letter_heights = []

    for letter in word:
        index = ord(letter) - ord('a')
        letter_heights.append(h[index])

    tallest = max(letter_heights)
    width = len(word)

    return tallest * width