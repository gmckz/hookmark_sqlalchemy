import "./App.css";
import { Routes, Route } from "react-router-dom";
import Project from "../Project/Project";
import Projects from "../Projects/Projects";
import AddProject from "../AddProject/AddProject";
import NavBar from "../NavBar/NavBar";

function App() {
	return (
		<>
			<NavBar />
			<div className="app">
				<Routes>
					<Route path="/projects/:id" element={<Project />} />
					<Route path="/projects" element={<Projects />} />
					<Route path="/add-project" element={<AddProject />} />
				</Routes>
			</div>
		</>
	);
}

export default App;
