import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

function Project() {
	const { id } = useParams();
	console.log(id);
	const URL = `http://127.0.0.1:5000/projects/${id}`;
	const [project, setProject] = useState({
		created_at: "",
		id: 0,
		link: "",
		name: "",
		notes: "",
	});

	useEffect(() => {
		console.log("fetching data");
		fetch(URL, {
			mode: "cors",
		})
			.then((res) => res.json())
			.then((data) =>
				setProject({
					created_at: data.created_at,
					id: data.id,
					link: data.link,
					name: data.name,
					notes: data.notes,
				})
			);
	}, []);

	console.log("logging project data:", project);
	return (
		<>
			<h1>{project.name}</h1>
			<div className="Pattern Link">
				<h2>Pattern link:</h2>
				<a href={project.link}>{project.link}</a>
			</div>
			<div className="Pattern Notes">
				<h2>Notes</h2>
				<p>{project.notes}</p>
			</div>
		</>
	);
}

export default Project;
