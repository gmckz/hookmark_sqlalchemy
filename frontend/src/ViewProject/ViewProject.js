import { useNavigate } from "react-router-dom";

function ViewProject({ project, setEditMode, URL }) {
	const navigate = useNavigate();
	const handleDelete = () => {
		const confirmDelete = window.confirm(
			"Are you sure you want to delete this project?"
		);
		if (confirmDelete) {
			fetch(URL, {
				method: "DELETE",
			}).then(() => navigate("/projects"));
		}
	};
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
					<button className="destructive" onClick={handleDelete}>
						Delete
					</button>
				</div>
			</div>
		</>
	);
}

export default ViewProject;
