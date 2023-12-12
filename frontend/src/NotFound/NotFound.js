import { Link } from "react-router-dom";

function NotFound() {
	return (
		<div>
			<h2>Oops!</h2>
			<p>That page can't be found.</p>
			<Link to="/projects">Go to All Projects...</Link>
		</div>
	);
}

export default NotFound;
