import React, { Component } from "react";
import Input from "@material-ui/core/Input";
import { Button } from "@material-ui/core";

import UploadButtons from "./UploadButton";

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
          <Button color="secondary" variant="contained">
            <Input type="file" name="file" />
          </Button>
          <Button color="primary" variant="contained">
            <Input type="submit" />
          </Button>
          <UploadButtons />
        </form>
      </div>
    );
  }
}
export default Form;
