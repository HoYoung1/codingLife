def emitPhotoData(outStream, photo):
    outStream.write(f'<p>제목: ${photo.title}</p>\n')
    outStream.write(f'<p>날짜: ${photo.date.toDateString()}</p>\n')


def renderPhoto(outStream, photo):
    pass


def renderPerson(outStream, person):
    outStream.write(f'<p>${person.name}</p>\n')
    renderPhoto(outStream, person.photo)
    emitPhotoData(outStream, person.photo)
    outStream.write(f'<p>위치: ${person.photo.location}</p>\n')  #


def recentDateCutoff():
    pass


def listRecentPhotos(outStream, photos):
    for p in filter(lambda p: p.date > recentDateCutoff(), photos):
        outStream.write("<div>\n")
        emitPhotoData(outStream, p)
        outStream.write(f'<p>위치: ${p.location}</p>\n')  #
        outStream.write("</div>\n")
