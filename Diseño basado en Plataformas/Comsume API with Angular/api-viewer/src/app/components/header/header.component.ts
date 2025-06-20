import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatInputModule,
    MatFormFieldModule,
    FormsModule,
    RouterLink
  ],
  template: `
    <mat-toolbar color="primary" class="header">
      <a routerLink="/" class="logo">
        <span class="app-title">CineExplorer</span>
      </a>
      <span class="spacer"></span>
      <div class="search-container">
        <mat-form-field appearance="outline">
          <mat-label>Buscar películas</mat-label>
          <input matInput [(ngModel)]="searchQuery" (keyup.enter)="search()">
          <mat-icon matSuffix>search</mat-icon>
        </mat-form-field>
        <button mat-raised-button color="accent" (click)="search()">Buscar</button>
      </div>
    </mat-toolbar>
  `,
  styles: [`
    .header {
      display: flex;
      align-items: center;
      padding: 0 16px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
      position: sticky;
      top: 0;
      z-index: 1000;
    }
    .logo {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: white;
    }
    .app-title {
      font-size: 1.5rem;
      font-weight: 600;
      margin-left: 8px;
    }
    .spacer {
      flex: 1 1 auto;
    }
    .search-container {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    mat-form-field {
      width: 300px;
      margin-bottom: -1.25em;
    }
    mat-form-field ::ng-deep .mat-mdc-form-field-subscript-wrapper {
      display: none;
    }
  `]
})
export class HeaderComponent {
  searchQuery: string = '';

  constructor(private router: Router) { }

  search() {
    if (this.searchQuery.trim()) {
      this.router.navigate(['/search'], { 
        queryParams: { query: this.searchQuery.trim() } 
      });
    }
  }
}
