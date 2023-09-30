# run ner model on all the ingredients name present in recipe of mongodb database and save it as ner_1

# iteration #1 : 

from batch_helper import *

#step #1 : load model and sanity check

# Reimplement the logic to find the path where stanza_corenlp is installed.
core_nlp_path = os.getenv('CORENLP_HOME', str(Path.home() / 'stanza_corenlp'))

# A heuristic to find the right jar file
classpath = [str(p) for p in Path(core_nlp_path).iterdir() if re.match(r"stanford-corenlp-[0-9.]+\.jar", p.name)][0]
# print(classpath)

# load model
model_name = 'ar'
model_file = f'/home/himani/cooking/notebooks/{model_name}.model.ser.gz'
ner_prop_filename = f'/home/himani/cooking/notebooks/{model_name}.model.props'

# sanity check
# annotations = annotate_ner(model_file,
#                            ["1 cup pineapple chunks ",
#                             "1 cup coconut milk ",
#                             "1⁄4 cup ice cubes ",
#                             "1⁄2 medium banana "])

# check annotation
# print(annotations[0])

# check tokens
# tokens = [token for sentence in annotations[0].sentence for token in sentence.token]
# print(tokens)

# check ner
# for t in tokens:
    # print(t.coarseNER, ':', t.word)
# print(annotations[2].sentence[0].token[3])

#step #2 : convert pdf 2 text

# read 1st file
files_list = os.listdir("/home/himani/cooking/books/")
files_list.sort()

files_loc = "/home/himani/cooking/books/"
first_file = files_list[-1]

# creating a pdf file object
pdfFileObj = open(files_loc + '/' + first_file, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

book_data = []

# printing number of pages in pdf file
for page_no in range(len(pdfReader.pages)):

    print('9999-99-99 99:99:99 INFO: page no-', page_no)

    # creating a page object
    pageObj = pdfReader.pages[page_no]

    # extracting text from page
    text = pageObj.extract_text()
    # text_split = text.split()
    # print(text)

    annotations = annotate_ner(model_file, [text])
    # print(annotations)

    if len(annotations) == 1:
        # print(extract_ner_data(annotations[0]))

        # check annotation
        # print(annotations[0])

        # check tokens
        tokens = [token for sentence in annotations[0].sentence for token in sentence.token]
        # print(tokens)

        ners = []
        words = []

        # check ner
        for t in tokens:
            # print(t.coarseNER, ':', t.word)
            ners.append(t.coarseNER)
            words.append(t.word)
    else:
        print('9999-99-99 99:99:99 INFO: annotations contain more than 1 text')

    book_data.append({'text': text, 'ners':ners, 'words':words})
    # print(book_data)

    # if page_no == 5:
    #     break

print('9999-99-99 99:99:99 INFO: Saving into Pandas Dataframe')

book_df = pd.DataFrame(book_data)
book_df.to_csv(first_file+'.csv', index=None)