import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthorizationService } from 'app/services/Auth/authorization.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html'
})
export class LoginComponent implements OnInit {

  formGroup: FormGroup;


  constructor(private fb: FormBuilder, private backend: AuthorizationService, private router:Router) {
    this.formGroup = fb.group({
      username: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
    });
   }

  ngOnInit(): void {
  }

  onLogIn(): void{
    console.log(this.formGroup.getRawValue());
    this.backend.login(this.formGroup.getRawValue()).then(
      (user) => {
        console.log(user);
        localStorage.setItem('token', user.Authorization);
        if (localStorage.token) {
          this.router.navigate(['/dashboard']);
          console.log(localStorage.token);
        }
        else {
        }
      }
    );
  }

  register() {
    this.router.navigate(['register']);
  }

}
