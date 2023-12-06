import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import "./Project.css";

function Project() {
	const { id } = useParams();
	const URL = `http://127.0.0.1:5000/projects/${id}`;
	const [project, setProject] = useState({
		created_at: "",
		id: 0,
		link: "",
		name: "",
		notes: "",
	});

	useEffect(() => {
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

	return (
		<>
			<div className="single-project">
				<h1>{project.name}</h1>
				<div className="pattern-link">
					<h2>Pattern link:</h2>
					<a href={project.link}>{project.link}</a>
				</div>
				<div className="pattern-notes">
					<h2>Notes</h2>
					<p>{project.notes}</p>
				</div>
				<button className="btn">Edit</button>
			</div>
		</>
	);
}

export default Project;
