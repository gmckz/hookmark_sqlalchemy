import "./ProjectForm.css";

function ProjectForm() {
	return (
		<>
			<div className="project-form-container">
				<h1>Add a new project</h1>
				<form className="project-form">
					<label>Project name:</label>
					<input type="text" required />
					<label>Pattern link:</label>
					<input type="text" required />
					<label>Notes:</label>
					<textarea required></textarea>
					<button>Add project</button>
				</form>
			</div>
		</>
	);
}

export default ProjectForm;
