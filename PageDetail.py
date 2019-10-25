import Search_page
def main():
    drug_link = Search_page.main()[0][0][3]
    URL = drug_link
    soup = Search_page.get_page(URL,None,None)


if __name__ == '__main__':
    main()