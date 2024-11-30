# %%

# pdf 내 이미지, 테이블
# pyMuPDF
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFium2Loader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredPowerPointLoader


# %%
loaderc = CSVLoader('./SP500_NOV2019_Hist.csv')
data = loaderc.load()
print(data)

type(data)
data[0].metadata['source']
data[0].page_content

# %%
#  + txt to docx 변환 or 일반 docx. 파일 사용

loaderd = Docx2txtLoader('./[이슈리포트 2022-2호] 혁신성장 정책금융 동향.docx')
data = loaderd.load()
data = loaderd.load_and_split()

# %%
# loderp = UnstructuredPowerPointLoader('./[이슈리포트 2022-2호] 혁신성장 정책금융 동향.pptx')

# %%

loaderw = WebBaseLoader('https://news.naver.com', encoding='utf-8',
                        bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                            class_=("comp_news_feed comp_news_none")))
                        )
loaderw.requests_per_second = {'verify': False}
data = loaderw.load()
data
# %%
data[0].metadata['description']
# %%

type(data[0].page_content)
# %%
rslt = data[0].page_content
# %%
rslt.split('\n')
# %%

[item for item in data[0].page_content.split('\n') if item]
# %%
rslt = [item for item in data[0].page_content.split(
    '\n') if item and item not in ['구독', '영상']]
# %%
len(rslt)
# %%
