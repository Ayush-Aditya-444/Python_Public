class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split()
        for i in range(len(title)):
            if len(title[i])>=3:
                title[i]=list(title[i])
                for j in range(1,len(title[i])):
                    title[i][0]=title[i][0].upper()
                    title[i][j]=title[i][j].lower()
            else:
                title[i]=title[i].lower()
            title[i]="".join(title[i])
        return " ".join(title)