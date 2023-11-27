import "./App.css";
import { Routes, Route } from "react-router-dom";
import Project from "./Project";
import Projects from "./Projects";

function App() {
	return (
		<Routes>
			<Route path="/projects/:id" element={<Project />} />
			<Route path="/projects" element={<Projects />} />
		</Routes>
	);
}

export default App;
