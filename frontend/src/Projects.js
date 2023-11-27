import { useState, useEffect } from "react";

function Projects() {
	const URL = "http://127.0.0.1:5000/projects";
	const [projects, setProjects] = useState([]);

	useEffect(() => {
		fetch(URL, {
			mode: "cors",
		})
			.then((res) => res.json())
			.then((data) => {
				setProjects(data.projects);
			});
	}, []);
	console.log("logging projects", projects);

	return (
		<>
			<h1>All Projects</h1>

			{projects.map((project) => {
				return (
					<div key={project.id} className="project">
						<h2>{project.name}</h2>
						<a
							href={`http://localhost:3000/projects/${project.id}`}
						>
							View Project
						</a>
					</div>
				);
			})}
		</>
	);
}

export default Projects;
