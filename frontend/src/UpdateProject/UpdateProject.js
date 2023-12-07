function UpdateProject({
	project,
	setEditMode,
	useState,
	id,
	setTrigger,
	trigger,
}) {
	const [name, setName] = useState(project.name);
	const [link, setLink] = useState(project.name);
	const [notes, setNotes] = useState(project.name);

	const handleSubmit = (e) => {
		e.preventDefault();
		const project = { data: { id, name, link, notes } };

		fetch("http://127.0.0.1:5000/projects", {
			method: "PUT",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(project),
		}).then(() => {
			setEditMode(false);
			setTrigger(!trigger);
		});
	};

	return (
		<>
			<div className="project-form-container">
				<h1>Edit project</h1>
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
					<button>Save</button>
				</form>
				<button className="cancel" onClick={() => setEditMode(false)}>
					Cancel
				</button>
			</div>
		</>
	);
}

export default UpdateProject;
