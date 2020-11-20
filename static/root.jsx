const Router = ReactRouterDOM.BrowserRouter;
const Route =  ReactRouterDOM.Route;
const Link =  ReactRouterDOM.Link;
const Prompt =  ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const useParams = ReactRouterDOM.useParams;
const useHistory = ReactRouterDOM.useHistory;

function Homepage() {
    return <div> Welcome to my site </div>
  }
  
  function About() {
    return <div> A tiny react demo site </div>
  }
  
  function SearchBar() { 
    return (
    <div>
        <input type="text"></input>
    </div>
    )
  }
  
  function Search() {
    return (
        <div>  
          Search for stuff 
          <SearchBar/>
        </div>
      )
  }

  function App() {
    return (
      <Router>
        <nav>
          <ul>
            <li>
                <Link to="/"> Home </Link>
            </li>
            <li>
                <Link to="/about"> About </Link>
            </li>
            <li>
                <Link to="/search"> Search </Link>
            </li>
            <li>
                <Link to="/login"> Login </Link>
            </li>
          </ul>
        </nav>
        <div>
          <Switch>
            <Route path="/about">
              <About />
            </Route>
            <Route path="/search">
              <Search />
            </Route>
            <Route path="/">
              <Homepage />
            </Route>
          </Switch>
        </div>
      </Router>
    );
}

ReactDOM.render(<App />, document.getElementById('root'))