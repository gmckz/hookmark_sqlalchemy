import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import "./Project.css";
import ViewProject from "../ViewProject/ViewProject";

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

	return <ViewProject project={project} />;
}

export default Project;
