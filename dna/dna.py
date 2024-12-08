import csv
import sys
import os


def main():

# TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("ERROR: Usage = python ex_file csv_file text_file")
        sys.exit(1)



    
# TODO: Read database file into a variable
    #get path
    csv_path = sys.argv[1]
    directory = 'databases'
    
    #get full path by joining the current working directory with the file path
    full_path = os.path.join(os.getcwd(),directory, csv_path)
    
    #Check if the file exists
    if os.path.exists(full_path):
        #open the file
        with open(full_path, 'r') as file:
            reader = csv.reader(file)
            content_csv = list(reader)
    else:
        print(f"File '{csv_path}' not found.")
        sys.exit(2)



# TODO: Read DNA sequence file into a variable
    # get path
    txt_path = sys.argv[2]
    directory = 'sequences'
    #get full path 
    full_txt_path = os.path.join(os.getcwd(),directory, txt_path)

    #check if file exists
    if os.path.exists(full_txt_path):
        #open the file
        with open(full_txt_path, 'r') as file:
            content_txt = file.read()
    else:
        print(f"File '{txt_path}' not found.")
        sys.exit(3)



# TODO: Find longest match of each STR in DNA sequence
    length_content = len(content_csv) #24 namen
    length_content0 = len(content_csv[0]) #9 sequences
    long_match_list = []

    for i in range(length_content0):
      long_match_list.append(longest_match(content_txt, content_csv[0][i]))



# TODO: Check database for matching profiles
    count = 0

    for i in range(1, length_content):
        for j in range(1, length_content0):
            if long_match_list[j] != int(content_csv[i][j]):
                count = 0
                break
            else:
                count = count + 1
                if count == length_content0 - 1:
                    print("Match found: ",content_csv[i][0])
                    return 
                   
    if count != length_content0 -1 :
      print("Match not found")

    return





def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
