import React, { Component } from "react";

class Form extends Component {
  state = {
    x: [],
    t: [],
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(e.target);
  };
  render() {
    return (
      <div>
        <form
          method="POST"
          action="/test"
          encType="multipart/form-data"
          onSubmit={this.handleSubmit}
        >
        </form>
      </div>
    );
  }
}
export default Form;
