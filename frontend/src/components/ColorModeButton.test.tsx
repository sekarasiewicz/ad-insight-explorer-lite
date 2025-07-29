import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import { ColorModeButton } from './ColorModeButton'

describe('ColorModeButton', () => {
  it('renders the button', () => {
    render(<ColorModeButton />)

    const button = screen.getByRole('button')
    expect(button).toBeInTheDocument()
  })

  it('has correct accessibility attributes', () => {
    render(<ColorModeButton />)

    const button = screen.getByRole('button')
    expect(button).toHaveAttribute('aria-label')
  })

  it('has correct styling classes', () => {
    render(<ColorModeButton />)

    const button = screen.getByRole('button')
    expect(button).toHaveClass('fixed', 'top-4', 'right-4', 'z-50')
  })
})
