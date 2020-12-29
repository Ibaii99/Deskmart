import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { AuthorizationService } from './authorization.service';

@Injectable({
  providedIn: 'root'
})
export class LoginRedirectService {

  constructor(private auth: AuthorizationService, private router:Router) { }

  canActivate(): boolean {
    if (localStorage.getItem('token')) {
      this.router.navigateByUrl('dashboard');
      return false;
    }
    else {
      return true;
    }
  }
}
