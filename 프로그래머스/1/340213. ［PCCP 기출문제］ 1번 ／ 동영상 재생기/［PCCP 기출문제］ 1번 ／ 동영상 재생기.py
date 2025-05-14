def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(t):  # 문자열 "mm:ss"를 초 단위 정수로
        m, s = map(int, t.split(":"))
        return m * 60 + s

    def to_time(t):  # 초 단위 정수를 "mm:ss" 문자열로
        m, s = divmod(t, 60)
        return f"{m:02}:{s:02}"

    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)

    for cmd in commands:
        # 명령 이전에 오프닝 건너뛰기
        if op_start <= pos <= op_end:
            pos = op_end

        if cmd == "next":
            if video_len - pos <= 10:
                pos = video_len
            else:
                pos += 10
        elif cmd == "prev":
            if pos < 10:
                pos = 0
            else:
                pos -= 10

        # 명령 이후에도 오프닝 구간에 걸치면 다시 스킵
        if op_start <= pos <= op_end:
            pos = op_end

    return to_time(pos)
