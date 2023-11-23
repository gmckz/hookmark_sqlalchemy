import "./App.css";
import { Routes, Route } from "react-router-dom";
import Project from "./Project";

function App() {
	return (
		<Routes>
			<Route path="/projects/:id" element={<Project />} />
		</Routes>
	);
}

export default App;
