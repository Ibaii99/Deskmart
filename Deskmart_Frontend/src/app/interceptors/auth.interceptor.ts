import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Router } from '@angular/router';
import { NotificationsService } from 'app/services/Notification/notifications.service';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class AuthInterceptor implements HttpInterceptor {

  constructor(private router: Router, private toastr: ToastrService) {
    this.noti = new NotificationsService(this.toastr);
  }

  noti: NotificationsService;

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token: string = localStorage.getItem('token');

    let request = req;

    request = req.clone({
      headers: req.headers.set('Content-Type', 'application/json')
        .set('X-Api-Key', 'aa')
    });

    if (token) {
      request = req.clone({
        headers: req.headers.set('Content-Type', 'application/json')
          .set('X-Api-Key', 'aa')
          .set('Authorization', `Bearer ${token}`)
      });
    }

    console.log(request);

    return next.handle(request).pipe( tap(() => {},
      (err: any) => {
      if (err instanceof HttpErrorResponse) {
        if (err.status !== 401) {
         return;
        }
        this.noti.showNotification('top', 'center', "error", "Session expired", "Please re log in");
        localStorage.clear();
        localStorage.removeItem('token');
        this.router.navigate(['login']);
      }
    }));
  }

}
