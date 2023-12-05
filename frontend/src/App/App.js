import "./App.css";
import { Routes, Route } from "react-router-dom";
import Project from "../Project/Project";
import Projects from "../Projects/Projects";
import ProjectForm from "../ProjectForm/ProjectForm";

function App() {
	return (
		<Routes>
			<Route path="/projects/:id" element={<Project />} />
			<Route path="/projects" element={<Projects />} />
			<Route path="/project-form" element={<ProjectForm />} />
		</Routes>
	);
}

export default App;
