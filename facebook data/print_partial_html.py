import re
import math

repo = "E:/facebook 2018/messages/"
source_file_name = "345.html"

in_file_path = repo + source_file_name

body_tag_open_pattern = "<body>"
body_tag_close_pattern = "</body>"
contains_body_tag_open = re.compile(body_tag_open_pattern)
contains_body_tag_close = re.compile(body_tag_close_pattern)

is_body = False
wrapper = []
body = ""
with open(file=in_file_path, mode="r", encoding="utf8") as f_in:
    for line in f_in:
        if contains_body_tag_open.search(line):
            line_split = line.split("<body>")
            wrapper.append(line_split[0])
            wrapper.append("<body>")
            body += line_split[1]
            is_body = True
        elif contains_body_tag_close.search(line):
            line_split = line.split("</body>")
            body += line_split[0]
            # wrapper.append(line_split[1])
            is_body = False
        elif is_body is False:
            wrapper.append(line)
        else:
            body += (line)
f_in.close()

file_counter = 1
body_split = body.split("</div>")
last_line = len(body_split)
number_of_files = 100
lines_per_file = math.ceil(last_line / number_of_files)

for i in range(0, number_of_files):
    file_number = ""
    file_number += (len(str(number_of_files)) - len(str(i + 1))) * "0"
    file_number += str(i + 1)
    out_file_path = repo + "/output/output_" + file_number + ".html"
    f_out = open(file=out_file_path, mode="w", encoding="utf8")
    for line in wrapper:
        f_out.write(line)
    current_line = lines_per_file * (i)
    body_line = ""
    for j in range(current_line, current_line + lines_per_file):
        try:
            raw_line = body_split[j]
            refined_line = raw_line.replace("<img", "<img style=\"max-width:400px;max-height:400px\"")
            refined_line = refined_line.replace("<p>", "<p style=\"margin:2px;\">")
            body_line += refined_line + "</div>\n"
        except IndexError:
            pass
    f_out.write(body_line)
    f_out.write("</body></html>")
    f_out.close()
