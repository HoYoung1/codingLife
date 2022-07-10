def render_photo(param):
    pass


def render_person(out_stream, person):
    result = []
    result.append(f"<p>{person['name']}</p>")
    result.append(render_photo(person["photo"]))
    result.append(zznew(person["photo"]))
    return ''.join(result)


def photo_div(p):
    return '\n'.join([
        "<div>",
        zznew(p),
        "</div>",
    ])


def zznew(p):
    return ''.join([
        f"<p>제목: ${p['title']}</p>",  # 제목 출력
        f'<p>위치: ${p["location"]}</p>',
        f'<p>날짜: ${str(p["data"])}</p>',
    ])


