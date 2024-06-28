# # Define a function to process the text file
# def convert_to_single_line(input_file_path, output_file_path):
#     try:
#         # Open the input file for reading
#         with open(input_file_path, "r") as input_file:
#             # Read the content of the input file and remove newline characters
#             content = input_file.read().replace("\n", "")

#         # Open the output file for writing
#         with open(output_file_path, "w") as output_file:
#             # Write the modified content to the output file
#             output_file.write(content)

#         print(f"Conversion complete. Check the output file: {output_file_path}")

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")


# # Provide the input and output file paths
# input_file_path = "msft.txt"  # Change this to your input file's path
# output_file_path = "output.txt"  # Change this to your desired output file's path

# # Call the function to perform the conversion
# convert_to_single_line(input_file_path, output_file_path)


# # Define a function to process the text file
# from summarizer import generate_summary


# def convert_to_single_line(input_file_path, output_file_path):
#     try:
#         # Open the input file for reading
#         with open(input_file_path, "r") as input_file:
#             # Read the content of the input file and remove newline characters
#             content = input_file.read().replace("\n", "")

#         # Open the output file for writing
#         with open(output_file_path, "w") as output_file:
#             # Write the modified content to the output file
#             output_file.write(content)

#         print(f"Conversion complete. Check the output file: {output_file_path}")

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")


# # Provide the input and output file paths
# input_file_path = "msft.txt"  # Change this to your input file's path
# output_file_path = "output.txt"  # Change this to your desired output file's path

# # Call the function to perform the conversion
# convert_to_single_line(input_file_path, output_file_path)

# # Generate a summary from the converted file with a unique output file name
# generate_summary(
#     output_file_path, 5
# )  # You need to define your generate_summary function

from summarizer import generate_summary


# # Define a function to process the text file
# def convert_to_single_column(input_file_path, output_file_path):
#     try:
#         # Open the input file for reading
#         with open(input_file_path, "r") as input_file:
#             # Read the content of the input file and remove newline characters
#             lines = input_file.readlines()

#         # Open the output file for writing
#         with open(output_file_path, "w") as output_file:
#             # Write the modified content to the output file as one column
#             for line in lines:
#                 output_file.write(line.strip() + "\n")

#         print(
#             f"Conversion to a single column complete. Check the output file: {output_file_path}"
#         )

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")


# # Provide the input and output file paths
# input_file_path = "msft.txt"  # Change this to your input file's path
# output_file_path = "output.txt"  # Change this to your desired output file's path

# # Call the function to perform the conversion
# convert_to_single_column(input_file_path, output_file_path)

# generate_summary(output_file_path, 5)


# Define a function to process the text file
def convert_to_single_column(input_file_path, output_file_path):
    try:
        # Open the input file for reading
        with open(input_file_path, "r") as input_file:
            # Read the content of the input file and remove newline characters
            content = input_file.read().replace("\n", " ")

        # Open the output file for writing
        with open(output_file_path, "w") as output_file:
            # Write the modified content to the output file as a single column
            output_file.write(content)

        print(
            f"Conversion to a single column complete. Check the output file: {output_file_path}"
        )

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Provide the input and output file paths
input_file_path = "msft.txt"  # Change this to your input file's path
output_file_path = "output.txt"  # Change this to your desired output file's path

# Call the function to perform the conversion
convert_to_single_column(input_file_path, output_file_path)


generate_summary(output_file_path, 5)
