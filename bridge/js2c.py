# https://webui.me
# https://github.com/webui-dev/webui
# Copyright (c) 2020-2025 Hassan Draga.
# Licensed under MIT License.
# All rights reserved.
# Canada.
#
# WebUI JavaScript to C Header

def js_to_c_header(input_filename, output_filename):
    try:
        print(f"Converting '{input_filename}' to '{output_filename}'...")

        # comment
        comment = (
            "// WebUI v2.5.0-beta.4\n"
            "// https://webui.me\n"
            "// https://github.com/webui-dev/webui\n"
            "// Copyright (c) 2020-2025 Hassan Draga.\n"
            "// Licensed under MIT License.\n"
            "// All rights reserved.\n"
            "// Canada.\n\n"
        )

        # Read JS file content
        with open(input_filename, 'r', encoding='utf-8') as file_js:
            content = file_js.read()
            file_js.close()        

        # Add comment to js
        new_content = comment + content
        with open(input_filename, 'w') as file_js:
            file_js.write(new_content)
            file_js.close()        

        # Convert each character in JS content to its hexadecimal value
        hex_values = ["0x{:02x}".format(ord(char)) for char in new_content]

        # Prepare the content for the C header file
        header_content = (
            comment + 
            "// --- PLEASE DO NOT EDIT THIS FILE -------\n"
            "// --- THIS FILE IS GENERATED BY JS2C.PY --\n\n"
            "#ifndef WEBUI_BRIDGE_H\n"
            "#define WEBUI_BRIDGE_H\n"
            "unsigned char webui_javascript_bridge[] = { "
        )

        # Split the hexadecimal values to make the output more readable, adding a new line every 10 values
        for i in range(0, len(hex_values), 10):
            header_content += "\n    " + ', '.join(hex_values[i:i+10]) + ','
        header_content += "\n    0x00\n};\n\n#endif // WEBUI_BRIDGE_H"

        # Write the header content to the output file
        with open(output_filename, 'w', encoding='utf-8') as file_h:
            file_h.write(header_content)
            file_h.close()

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return

# Main
js_to_c_header('webui.js', 'webui_bridge.h')
