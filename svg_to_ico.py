#!/usr/bin/env python3
"""
SVG to ICO converter script
Converts favicon.svg to favicon.ico with multiple sizes
"""

import cairosvg
from PIL import Image
import io
import os

def svg_to_ico(svg_file, ico_file, sizes=[16, 32, 48]):
    """
    Convert SVG to ICO with multiple sizes
    
    Args:
        svg_file (str): Path to input SVG file
        ico_file (str): Path to output ICO file  
        sizes (list): List of icon sizes to include
    """
    try:
        # Read SVG file
        with open(svg_file, 'rb') as f:
            svg_data = f.read()
        
        # Create images for different sizes
        images = []
        
        for size in sizes:
            # Convert SVG to PNG at specific size
            png_data = cairosvg.svg2png(
                bytestring=svg_data,
                output_width=size,
                output_height=size
            )
            
            # Open PNG data as PIL Image
            img = Image.open(io.BytesIO(png_data))
            
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
                
            images.append(img)
            print(f"Generated {size}x{size} icon")
        
        # Save as ICO file with multiple sizes
        images[0].save(
            ico_file,
            format='ICO',
            sizes=[(img.width, img.height) for img in images],
            append_images=images[1:]
        )
        
        print(f"Successfully created {ico_file}")
        
        # Show file info
        file_size = os.path.getsize(ico_file)
        print(f"File size: {file_size} bytes")
        
    except Exception as e:
        print(f"Error converting SVG to ICO: {e}")
        return False
        
    return True

if __name__ == "__main__":
    # Convert favicon.svg to favicon.ico
    svg_file = "favicon.svg"
    ico_file = "favicon.ico"
    
    if not os.path.exists(svg_file):
        print(f"Error: {svg_file} not found")
        exit(1)
    
    # Convert with standard favicon sizes
    success = svg_to_ico(svg_file, ico_file, sizes=[16, 24, 32, 48])
    
    if success:
        print(f"\n✅ Successfully converted {svg_file} to {ico_file}")
        print("You can now use favicon.ico in your website!")
    else:
        print(f"\n❌ Failed to convert {svg_file}") 