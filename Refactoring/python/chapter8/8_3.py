def render_photo(param):
    pass


def render_person(out_stream, person):
    result = []
    result.append(f"<p>{person['name']}</p>")
    result.append(render_photo(person["photo"]))
    result.append(f"<p>제목: ${person['photo']['title']}</p>")
    result.append(emit_photo_data(person['photo']))
    return ''.join(result)


def photo_div(p):
    return '\n'.join([
        "<div>",
        f"<p>제목: ${p['title']}</p>",  # 제목 출력
        emit_photo_data(p),
        "</div>",
    ])


def emit_photo_data(aPhoto):
    result = []
    result.append(f'<p>위치: ${aPhoto["location"]}</p>')
    result.append(f'<p>날짜: ${str(aPhoto["data"])}</p>')
    return '\n'.join(result)
