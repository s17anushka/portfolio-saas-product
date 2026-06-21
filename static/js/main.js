document.addEventListener('DOMContentLoaded', () => {
    fetchProjects();
});

async function fetchProjects() {
    const grid = document.getElementById('projects-grid');
    try {
        const response = await fetch('/api/projects');
        const projects = await response.json();
        
        grid.innerHTML = ''; 
        
        if (projects.length === 0) {
            grid.innerHTML = `<p class="text-gray-500">No projects found.</p>`;
            return;
        }

        projects.forEach(project => {
            const card = document.createElement('div');
            card.className = 'bg-gray-800/50 backdrop-blur-md p-6 rounded-2xl border border-gray-700/50 flex flex-col justify-between hover:border-blue-500/50 transition-all duration-300 shadow-xl';
            
            const tags = project.tech_stack.map(tech => 
                `<span class="bg-blue-500/10 text-blue-400 text-xs font-semibold px-3 py-1 rounded-full border border-blue-500/20">${tech}</span>`
            ).join('');

            card.innerHTML = `
                <div>
                    <h4 class="text-xl font-bold text-white mb-2 tracking-tight">${project.title}</h4>
                    <p class="text-gray-400 text-sm leading-relaxed mb-4">${project.description}</p>
                    <div class="flex flex-wrap gap-2 mb-6">${tags}</div>
                </div>
                <div class="flex items-center justify-between text-sm pt-4 border-t border-gray-700/30">
                    ${project.github_link ? `<a href="${project.github_link}" target="_blank" class="text-gray-300 hover:text-white transition font-medium flex items-center gap-1">Code ↗</a>` : ''}
                    ${project.live_link ? `<a href="${project.live_link}" target="_blank" class="text-blue-400 hover:text-blue-300 transition font-medium flex items-center gap-1">Live Demo →</a>` : ''}
                </div>
            `;
            grid.appendChild(card);
        });
    } catch (error) {
        console.error('Error fetching projects:', error);
        grid.innerHTML = `<p class="text-red-400">Failed to load projects.</p>`;
    }
}