import "./NavBar.css";

function NavBar() {
	return (
		<>
			<nav className="navbar">
				<h1>hookmark</h1>
				<div className="navbar-links">
					<a href="/projects">All Projects</a>
					<a href="/add-project">Add Project</a>
				</div>
			</nav>
		</>
	);
}

export default NavBar;
