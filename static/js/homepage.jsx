"use strict";

function Homepage() {
    return (
        <React.Fragment>
            <div>
              <h1>Log In</h1>
            </div>
            <div>
              <form action="/profile" method="POST">
                Email: <input type="text" name="email" required></input> <br/>
                Password: <input type="password" name="password" required></input> <br/>
                <button type="submit">Log In</button> <br/>
                <br/>
              </form>
                Don't have an account yet? <a href="/create-account">Create an Account</a>
            </div>
        </React.Fragment>
    );
}

ReactDOM.render(<Homepage />, document.querySelector('#homepage'));