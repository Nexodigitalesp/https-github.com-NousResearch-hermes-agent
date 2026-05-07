import csv
import sys
import json

def generate_message(template, lead_data):
    """
    Generates a message from a template and lead data.
    In a real scenario, this would call an LLM API.
    """
    try:
        return template.format(**lead_data)
    except KeyError as e:
        return f"Error: Missing variable {e}"

def process_bulk(csv_path, template_path, output_path):
    """
    Processes a CSV of leads and generates messages using a template.
    """
    with open(template_path, 'r') as f:
        template = f.read()

    results = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            message = generate_message(template, row)
            row['generated_message'] = message
            results.append(row)

    if results:
        keys = results[0].keys()
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)
        print(f"Successfully generated {len(results)} messages to {output_path}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python bulk_generator.py <leads_csv> <template_file> <output_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    template_path = sys.argv[2]
    output_path = sys.argv[3]

    process_bulk(csv_path, template_path, output_path)

if __name__ == "__main__":
    main()
