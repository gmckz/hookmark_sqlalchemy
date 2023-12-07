import "./AddProject.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function AddProject() {
	const [name, setName] = useState("");
	const [link, setLink] = useState("");
	const [notes, setNotes] = useState("");
	const [isPending, setIsPending] = useState(false);
	const navigate = useNavigate();

	const handleSubmit = (e) => {
		e.preventDefault();
		const project = { data: { name, link, notes } };
		setIsPending(true);

		fetch("http://127.0.0.1:5000/projects", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(project),
		})
			.then((res) => res.json())
			.then((data) => {
				console.log(data.id);
				setIsPending(false);
				navigate(`/projects/${data.id}`);
			});
	};

	return (
		<>
			<div className="project-form-container">
				<h1>Add a new project</h1>
				<form className="project-form" onSubmit={handleSubmit}>
					<label>Project name:</label>
					<input
						type="text"
						required
						value={name}
						onChange={(e) => setName(e.target.value)}
					/>
					<label>Pattern link:</label>
					<input
						type="text"
						required
						value={link}
						onChange={(e) => setLink(e.target.value)}
					/>
					<label>Notes:</label>
					<textarea
						value={notes}
						onChange={(e) => setNotes(e.target.value)}
					></textarea>
					{!isPending && <button>Add project</button>}
					{isPending && <button disabled>Adding project...</button>}
				</form>
			</div>
		</>
	);
}

export default AddProject;
