import string
import itertools
import multiprocessing
import time

def generate_codes(length):
    # Generate all possible alphanumeric codes of given length
    characters = string.ascii_letters + string.digits
    codes = [''.join(code) for code in itertools.product(characters, repeat=length)]
    return codes

def check_codes(codes):
    for code in codes:
        if code == target_code:
            return code
    return None

def decode_code(target_code):
    code_length = len(target_code)
    codes = generate_codes(code_length)

    print("Decoding in progress...")

    start_time = time.time()

    # Create a multiprocessing pool with maximum available processors
    pool = multiprocessing.Pool()

    batch_size = 1000
    code_batches = [codes[i:i+batch_size] for i in range(0, len(codes), batch_size)]

    # Use multiprocessing map function to check code batches in parallel
    results = pool.map(check_codes, code_batches)

    # Close the pool to free up resources
    pool.close()

    # Check the results for a valid code
    code_found = next((result for result in results if result is not None), None)

    if code_found:
        elapsed_time = time.time() - start_time
        print(f"Code found: {code_found}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
    else:
        print("Code not found.")

# Example usage
target_code = input("Enter the alphanumeric code to decode: ")
decode_code(target_code)
