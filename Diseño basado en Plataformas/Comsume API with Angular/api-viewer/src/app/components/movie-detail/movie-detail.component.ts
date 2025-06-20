import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { MovieDetail } from '../../models/movie.model';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatIconModule } from '@angular/material/icon';
import { MatChipsModule } from '@angular/material/chips';
import { MatDividerModule } from '@angular/material/divider';

@Component({
  selector: 'app-movie-detail',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    MatProgressSpinnerModule,
    MatIconModule,
    MatChipsModule,
    MatDividerModule
  ],
  template: `
    <div class="container">
      <button mat-button color="primary" class="back-button" (click)="goBack()">
        <mat-icon>arrow_back</mat-icon> Volver
      </button>
      
      <div *ngIf="loading" class="loading-container">
        <mat-spinner></mat-spinner>
      </div>
      
      <div *ngIf="!loading && movie" class="movie-detail">
        <div class="backdrop" [style.background-image]="'url(' + getBackdropUrl() + ')'">
          <div class="backdrop-overlay"></div>
        </div>
        
        <div class="content">
          <div class="poster-container">
            <img [src]="movieService.getImageUrl(movie.poster_path)" [alt]="movie.title" class="poster">
            <div class="rating">
              <div class="rating-circle">
                {{ movie.vote_average | number:'1.1-1' }}
              </div>
              <span class="rating-text">User Score</span>
            </div>
          </div>
          
          <div class="info">
            <h1 class="title">{{ movie.title }} <span class="year" *ngIf="movie.release_date">({{ getYear(movie.release_date) }})</span></h1>
            
            <p class="release-info">
              {{ movie.release_date | date:'mediumDate' }} • 
              <span *ngIf="movie.runtime">{{ formatRuntime(movie.runtime) }}</span>
            </p>
            
            <div class="genres">
              <mat-chip-set>
                <mat-chip *ngFor="let genre of movie.genres">{{ genre.name }}</mat-chip>
              </mat-chip-set>
            </div>
            
            <p class="tagline" *ngIf="movie.tagline">{{ movie.tagline }}</p>
            
            <h3 class="section-title">Sinopsis</h3>
            <p class="overview">{{ movie.overview }}</p>
            
            <mat-divider></mat-divider>
            
            <div class="additional-info">
              <div class="info-item" *ngIf="movie.status">
                <h4>Estado</h4>
                <p>{{ movie.status }}</p>
              </div>
              
              <div class="info-item" *ngIf="movie.budget">
                <h4>Presupuesto</h4>
                <p>{{ movie.budget | currency }}</p>
              </div>
              
              <div class="info-item" *ngIf="movie.revenue">
                <h4>Ingresos</h4>
                <p>{{ movie.revenue | currency }}</p>
              </div>
            </div>
            
            <div class="actions" *ngIf="movie.homepage">
              <a mat-raised-button color="primary" [href]="movie.homepage" target="_blank">
                <mat-icon>language</mat-icon> Sitio Web Oficial
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
      position: relative;
    }
    .back-button {
      margin-bottom: 20px;
    }
    .loading-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 300px;
    }
    .movie-detail {
      position: relative;
      background-color: white;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .backdrop {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 500px;
      background-size: cover;
      background-position: center top;
      z-index: 0;
    }
    .backdrop-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.6) 100%);
    }
    .content {
      position: relative;
      z-index: 1;
      display: flex;
      padding: 30px;
      color: white;
    }
    .poster-container {
      flex: 0 0 300px;
      margin-right: 30px;
      position: relative;
    }
    .poster {
      width: 100%;
      border-radius: 8px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    .info {
      flex: 1;
    }
    .title {
      font-size: 2.5rem;
      margin: 0 0 10px;
      color: white;
    }
    .year {
      font-weight: 400;
      opacity: 0.9;
    }
    .release-info {
      font-size: 1.1rem;
      margin-bottom: 15px;
      color: rgba(255,255,255,0.8);
    }
    .genres {
      margin-bottom: 20px;
    }
    .tagline {
      font-style: italic;
      font-size: 1.2rem;
      margin-bottom: 20px;
      color: rgba(255,255,255,0.9);
    }
    .section-title {
      font-size: 1.5rem;
      margin-bottom: 10px;
      color: white;
    }
    .overview {
      font-size: 1.1rem;
      line-height: 1.6;
      margin-bottom: 30px;
      color: rgba(255,255,255,0.9);
    }
    .additional-info {
      display: flex;
      flex-wrap: wrap;
      gap: 30px;
      margin: 30px 0;
      color: white;
    }
    .info-item {
      flex: 1;
      min-width: 200px;
    }
    .info-item h4 {
      font-size: 1.1rem;
      margin: 0 0 10px;
      color: rgba(255,255,255,0.8);
    }
    .info-item p {
      font-size: 1.2rem;
      margin: 0;
    }
    .actions {
      margin-top: 20px;
    }
    .rating {
      position: absolute;
      top: 20px;
      left: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .rating-circle {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background-color: rgba(0,0,0,0.8);
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 1.5rem;
      font-weight: bold;
      margin-bottom: 5px;
      border: 3px solid #4CAF50;
    }
    .rating-text {
      font-size: 0.9rem;
      color: white;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.7);
    }
    
    /* Responsive styles */
    @media (max-width: 768px) {
      .content {
        flex-direction: column;
      }
      .poster-container {
        margin-right: 0;
        margin-bottom: 20px;
        max-width: 70%;
        align-self: center;
      }
      .title {
        font-size: 2rem;
      }
    }
  `]
})
export class MovieDetailComponent implements OnInit {
  movie: MovieDetail | null = null;
  loading = true;

  constructor(
    public movieService: MovieService,
    private route: ActivatedRoute,
    private router: Router
  ) { }
  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const idParam = params.get('id');
      console.log('Movie ID from route:', idParam);
      
      if (idParam) {
        const id = Number(idParam);
        console.log('Converted ID:', id);
        this.loadMovieDetails(id);
      } else {
        console.error('No ID parameter found');
        this.router.navigate(['/']);
      }
    });
  }

  loadMovieDetails(id: number): void {
    this.loading = true;
    console.log(`Loading movie details for ID: ${id}`);
    
    this.movieService.getMovieDetails(id).subscribe({
      next: (movie) => {
        console.log('Movie details loaded successfully:', movie);
        this.movie = movie;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading movie details', error);
        this.loading = false;
        this.router.navigate(['/']);
      }
    });
  }

  getBackdropUrl(): string {
    if (this.movie && this.movie.backdrop_path) {
      return this.movieService.getImageUrl(this.movie.backdrop_path, 'original');
    }
    return '';
  }

  formatRuntime(minutes: number): string {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}h ${mins}m`;
  }

  getYear(dateString: string): string {
    return new Date(dateString).getFullYear().toString();
  }

  goBack(): void {
    this.router.navigate(['/']);
  }
}
