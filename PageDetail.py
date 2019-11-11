import Search_page
from Search_page import get_result


def get_pageDetail(soup):
    page_content = []
    if soup.find(id='medinfo-cureitem_s-text') is None:  # 0
        page_content.append(soup.find(id='medinfo-cureitem-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-cureitem_s-text').get_text(strip=True))
    if soup.find(id='medinfo-aftereffect_s-text') is None:  # 1
        page_content.append(soup.find(id='medinfo-aftereffect-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-aftereffect_s-text').get_text(strip=True))
    if soup.find(id='medinfo-careitem_s-text') is None:  # 2
        page_content.append(soup.find(id='medinfo-careitem-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-careitem_s-text').get_text(strip=True))
    if soup.find(id='medinfo-contradictions_s-text') is None:  # 3
        page_content.append(soup.find(id='medinfo-contradictions-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-contradictions_s-text').get_text(strip=True))
    if soup.find(id='medinfo-mamiitem_s-text') is None:  # 4
        page_content.append(soup.find(id='medinfo-mamiitem-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-mamiitem_s-text').get_text(strip=True))
    if soup.find(id='medinfo-effect_s-text') is None:  # 5
        page_content.append(soup.find(id='medinfo-effect-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-effect_s-text').get_text(strip=True))
    if soup.find(id='medinfo-useway_s-text') is None:  # 6
        page_content.append(soup.find(id='medinfo-useway-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-useway_s-text').get_text(strip=True))
    if soup.find(id='medinfo-interaction_s-text') is None:  # 7
        page_content.append(soup.find(id='medinfo-interaction-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-interaction_s-text').get_text(strip=True))

    return page_content


def text_process(soup):
    # 3
    contradictions_raw = get_pageDetail(soup)[3]
    contradictions_list = contradictions_raw.split('。')
    # 4
    mamiitem_raw = get_pageDetail(soup)[4]
    mamiitem_list = mamiitem_raw.split('。')
    # 5
    effect_raw = get_pageDetail(soup)[5]
    effect_list = effect_raw.split('。')
    # 6
    useway_raw = get_pageDetail(soup)[6]
    useway_list = useway_raw.split('。')
    # 7
    interaction_raw = get_pageDetail(soup)[7]
    interaction_list = interaction_raw.split('。')

    return [contradictions_list, mamiitem_list, effect_list, useway_list, interaction_list]


def main():
    drug_link = Search_page.main()[0][0][3]
    URL = drug_link
    soup = Search_page.get_page(URL, str(None), None)
    print("適應症:" + '\n' + str(get_pageDetail(soup)[0]) + '\n')
    print("副作用:" + '\n' + str(get_pageDetail(soup)[1]) + '\n')
    print("警語:" + '\n' + str(get_pageDetail(soup)[2]) + '\n')
    print("使用禁忌:")
    for i in range(0, len(text_process(soup)[0]) - 1):
        print(text_process(soup)[0][i] + '。')
    print('\n')
    print("懷孕/授乳注意事項:")
    for i in range(0, len(text_process(soup)[1]) - 1):
        print(text_process(soup)[1][i] + '。')
    print('\n')
    print("藥理作用:")
    for i in range(0, len(text_process(soup)[2]) - 1):
        print(text_process(soup)[2][i] + '。')
    print('\n')
    print("用法用量:")
    for i in range(0, len(text_process(soup)[3]) - 1):
        print(text_process(soup)[3][i] + '。')
    print('\n')
    print("交互作用:")
    for i in range(0, len(text_process(soup)[4]) - 1):
        print(text_process(soup)[4][i] + '。')
    print('\n')


if __name__ == '__main__':
    while True:
        main()
