#!/usr/bin/env python3

# Read the current index.html
with open('index.html', 'r') as f:
    lines = f.readlines()

# Find the line numbers to replace (177-294, but in Python it's 176-293 since 0-indexed)
# We need to replace from line 177 (index 176) to line 294 (index 293)
start_line = 176  # Line 177 in 1-indexed
end_line = 293    # Line 294 in 1-indexed

# New content to insert
new_content = '''      <!-- Image Slider Container -->
      <div class="relative overflow-hidden h-96">
        <div class="project-slider flex transition-transform duration-700 ease-in-out h-full">
          
          <!-- Project Image 1 -->
          <a href="site/pdfs/Bachelors_Thesis.pdf" target="_blank" rel="noopener noreferrer" 
             class="project-slide min-w-full flex-shrink-0 h-full relative group cursor-pointer">
            <img src="site/images/mountain.avif" alt="Ancient Microbiomes Project" 
                 class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
              <div class="p-8">
                <h3 class="text-white text-2xl font-light mb-2">Ancient Microbiomes Analysis</h3>
                <p class="text-slate-300">Bachelor's Thesis - University of Bologna</p>
              </div>
            </div>
          </a>

          <!-- Project Image 2 -->
          <a href="site/pdfs/MethylationML.pdf" target="_blank" rel="noopener noreferrer"
             class="project-slide min-w-full flex-shrink-0 h-full relative group cursor-pointer">
            <img src="site/images/IMG_1580.png" alt="Methylation ML Project" 
                 class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
              <div class="p-8">
                <h3 class="text-white text-2xl font-light mb-2">Pan-Tissue Epigenetic Clock</h3>
                <p class="text-slate-300">Machine Learning Project</p>
              </div>
            </div>
          </a>

          <!-- Project Image 3 -->
          <a href="site/pdfs/Masters_Thesis.pdf" target="_blank" rel="noopener noreferrer"
             class="project-slide min-w-full flex-shrink-0 h-full relative group cursor-pointer">
            <img src="site/images/IMG_1445.jpeg" alt="Brain Connectivity Project" 
                 class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent flex items-end">
              <div class="p-8">
                <h3 class="text-white text-2xl font-light mb-2">Brain Connectivity Mapping</h3>
                <p class="text-slate-300">Master's Thesis - University of Amsterdam</p>
              </div>
            </div>
          </a>

        </div>
      </div>
    </div>
  </section>
'''

# Build the new file content
new_lines = lines[:start_line] + [new_content + '\n'] + lines[end_line + 1:]

# Write back to the file
with open('index.html', 'w') as f:
    f.writelines(new_lines)

print("Projects section replaced successfully!")
