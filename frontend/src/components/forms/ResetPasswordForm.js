import React from 'react';
import PropTypes from 'prop-types'
import {Form, Button, Message } from 'semantic-ui-react';
import isEmail from 'validator/lib/isEmail';
import InlineError from '../messages/InlineError';

class ResetPasswordForm extends React.Component{
  state = {
    data: {
      email: '',
      password: '',
      passwordconf: '',
      token: this.props.token
    },
    loading: false,
    errors: {}
  };

  onChange = e =>
    this.setState({
      data: {...this.state.data, [e.target.name]: e.target.value }
    });

  onSubmit = e => {
    e.preventDefault();
    const errors = this.validate(this.state.data);
    this.setState({errors});

    if (Object.keys(errors).length === 0) {
      this.setState({loading: true})
      this.props.submit(this.state.data)
        .catch(err => this.setState({errors: err, loading: false}));
    }
  }

  validate = (data) => {
    const errors = {};
    if (!isEmail(data.email)) errors.email = "Invalid Email";
    if (data.password !== data.passwordconf) errors.password = "Passwords don't match";
    return errors;
  }

  render() {
    const { errors, data, loading } = this.state;

    return (
      <Form onSubmit={this.onSubmit} loading={loading}>
        {!!errors.global && <Message negative>{errors.global}</Message>}
        <Form.Field error={!!errors.email}>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="email"
            value={data.email}
            onChange={this.onChange}
            />
          {errors.email && <InlineError text={errors.email} />}
        </Form.Field>

        <Form.Field error={!!errors.password}>
          <label htmlFor="password">New Password</label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="DogeCoin#1234"
            value={data.password}
            onChange={this.onChange}
            />
          {errors.password && <InlineError text={errors.password} />}
        </Form.Field>

        <Form.Field error={!!errors.password}>
          <label htmlFor="passwordconf">Password Confirmation</label>
          <input
            type="password"
            id="passwordconf"
            name="passwordconf"
            placeholder="DogeCoin#1234"
            value={data.passwordconf}
            onChange={this.onChange}
            />
          {errors.password && <InlineError text={errors.password} />}
        </Form.Field>



        <Button primary>Reset Password</Button>
      </Form>
    )
  }
}

ResetPasswordForm.propTypes = {
  submit: PropTypes.func.isRequired
}

export default ResetPasswordForm;
