function ViewProject({ project, setEditMode }) {
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
				<div className="btn-container">
					<button onClick={() => setEditMode(true)}>Edit</button>
					<button className="destructive">Delete</button>
				</div>
			</div>
		</>
	);
}

export default ViewProject;
