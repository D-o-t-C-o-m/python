import os
import pandas as pd
import tabula

folder = os.getcwd()

pdf_files = [f for f in os.listdir(folder) if f.endswith(".pdf")]

if not pdf_files:
    print("No PDF files found in the current directory.")
else:
    print("Choose a PDF file(s) to convert:")
    for i, pdf_file in enumerate(pdf_files):
        print("{}. {}".format(i + 1, pdf_file))
    print("{}. Convert all files".format(len(pdf_files) + 1))
    choice = int(input("Enter the number of the file(s) to convert: ")) - 1

    if choice == len(pdf_files):
        for pdf_file in pdf_files:
            dfs = tabula.read_pdf(os.path.join(folder, pdf_file), pages="all")
            result = pd.concat(dfs)

            output_file = os.path.splitext(pdf_file)[0] + ".csv"
            result.to_csv(os.path.join(folder, output_file), index=False)
    elif 0 <= choice < len(pdf_files):
        pdf_file = pdf_files[choice]

        dfs = tabula.read_pdf(os.path.join(folder, pdf_file), pages="all")
        result = pd.concat(dfs)

        output_file = os.path.splitext(pdf_file)[0] + ".csv"
        result.to_csv(os.path.join(folder, output_file), index=False)
    else:
        print("Invalid choice.")

print("Export Complete")