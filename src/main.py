import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

    # test = TextNode("bla", TextType.ITALIC, "https://test.com")
    # print(test)
    # ta = TextNode("**bold** and *italic*", TextType.TEXT)
    # print(ta.text.split("**"), ta.text.count("**"))
    # print(ta.text.partition("**"))
    # for item in ta.text.split("**"):
    #     print(item)
    # tb = TextNode("This is text with a **bolded word** and **another**", TextType.TEXT)
    # print(tb.text.split("**"), tb.text.count("**"))
    # print(tb.text.partition("**"))
    # for item in tb.text.split("**"):
    #     print(item)
    # md_img = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # md_url = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # md_test = TextNode(
    #     "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    #     TextType.TEXT,
    # )
    # print(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", md_img))
    # print(re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", md_test.text))
    # for m in re.finditer(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", md_test.text):
    # print(m)
    # print("%02d-%02d: %s" % (m.start(), m.end(), m.group(0)))

    # m = re.finditer(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", md_test.text)
    # print(m)


#     ml_str = f"""# This is a heading

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item"""
#     print(ml_str.splitlines())
#     print(ml_str.split("\n\n"))
#     print(list(filter(None, ml_str.splitlines())))


main()
