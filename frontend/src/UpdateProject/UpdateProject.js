function UpdateProject({ project, setEditMode, useState }) {
	const [name, setName] = useState(project.name);
	const [link, setLink] = useState(project.name);
	const [notes, setNotes] = useState(project.name);

	return (
		<>
			<div className="project-form-container">
				<h1>Add a new project</h1>
				<form className="project-form" /*onSubmit={handleSubmit}*/>
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
					<button>Add project</button>
				</form>
				<button className="btn" onClick={() => setEditMode(false)}>
					Cancel
				</button>
			</div>
		</>
	);
}

export default UpdateProject;
