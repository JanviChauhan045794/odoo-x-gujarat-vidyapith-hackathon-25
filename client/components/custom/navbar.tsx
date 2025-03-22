import { NavigationMenu, NavigationMenuItem, NavigationMenuList } from "@/components/ui/navigation-menu";
import Link from "next/link";
import { CalendarDays, LucideMenu } from "lucide-react"
import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui/hover-card"
import Image from "next/image";
import { LogoLabelComp } from "@/components/custom/logo-label";
import { Button } from "@/components/ui/button";
import { Drawer, DrawerClose, DrawerContent, DrawerFooter, DrawerHeader, DrawerTitle, DrawerTrigger, } from "@/components/ui/drawer"
import { pageLinks } from "@/lib/page-links";
import { SearchBarComp } from "./search";
import { assetsLinks } from "@/lib/assets-links";

/**
 * The Global Navbar component 
 */
export function NavbarComp() {
    const pages: { title: string, link: string }[] = [
        { title: "Products", link: pageLinks.nav.products },
        { title: "About", link: pageLinks.nav.about },
        { title: "Docs", link: pageLinks.nav.docs },
        { title: "Contact", link: pageLinks.resource.contact },
    ]
    return (
        <>
            <nav className="flex items-center justify-between bg-background w-full border-b border-b-border/20  z-50 h-16 overflow-hidden fixed px-5">

                {/*SECTION - Logo */}
                <div className="flex items-center space-x-4">
                    <HoverCard>
                        <HoverCardTrigger asChild>
                            <Link href={pageLinks.nav.home} passHref className="flex items-center space-x-2">
                                <Image src={assetsLinks.fraxation_logo.src} width={50} height={50} alt={assetsLinks.fraxation_logo.alt} />
                                <LogoLabelComp className="text-2xl hidden md:block" />
                            </Link>
                        </HoverCardTrigger>
                        <HoverCardContent className="w-80 bg-background text-foreground border-border/50">
                            <div className="mb-3">
                                <Image src={assetsLinks.fraxation_logo.src} width={200} height={200} alt={assetsLinks.fraxation_logo.alt} className="mx-auto" />
                                <LogoLabelComp className="text-4xl" />
                            </div>
                            <div className="flex justify-between space-x-4">
                                <div className="space-y-1">
                                    <h4 className="text-sm font-semibold">@fraxation</h4>
                                    <p className="text-sm">
                                        AI-Powered, Pre-Configured Development Tools for Faster Application Building.
                                    </p>
                                    <div className="flex items-center pt-2">
                                        <CalendarDays className="mr-2 h-4 w-4 opacity-70" />{" "}
                                        <span className="text-xs text-muted-foreground">
                                            Founded in 2025
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </HoverCardContent>
                    </HoverCard>
                    {/*!SECTION */}

                    {/*SECTION - Desktop Menu Bar */}
                    <NavigationMenu className="hidden lg:flex">
                        <NavigationMenuList>
                            <NavigationMenuItem className="group space-x-5 text-sm text-lime-100">
                                {pages.map((item, index) => (
                                    <Link className="py-2 px-3 hover:bg-lime-900/50 rounded-full" href={item.link} key={index}>{item.title}</Link>
                                ))}
                            </NavigationMenuItem>
                        </NavigationMenuList>
                    </NavigationMenu>
                </div>
                {/*!SECTION */}

                {/*SECTION - Navigation Side View*/}
                <NavigationMenu className="right-0">
                    <NavigationMenuList>
                        <NavigationMenuItem className="group space-x-5 flex-row">
                            {/* Navigation Menu Mobile bar*/}
                            <Drawer>
                                <div className="flex-row flex items-center space-x-2">
                                    <SearchBarComp />
                                    <Link href={pageLinks.auth.login} passHref>
                                        <Button>Log In</Button>
                                    </Link>
                                    <Link href={pageLinks.auth.signup} passHref>
                                        <Button className="hover:bg-lime-50 hover:text-lime-950" variant={"outline"} >Sign Up</Button>
                                    </Link>
                                    <DrawerTrigger className="flex lg:hidden"><LucideMenu /></DrawerTrigger>
                                </div>
                                <DrawerContent className="border-t">
                                    <div className="mx-auto md:w-5/6 w-full overflow-y-scroll no-scrollbar">
                                        <DrawerHeader className="space-y-1">
                                            <DrawerTitle></DrawerTitle>
                                            {pages.map((item, index) => (
                                                <Link href={item.link} className="bg-lime-900/50 text-lime-200 rounded-md px-4 py-2" key={index}>{item.title}</Link>
                                            ))}
                                        </DrawerHeader>
                                        <DrawerFooter>
                                            <DrawerClose>
                                            </DrawerClose>
                                        </DrawerFooter>
                                    </div>
                                </DrawerContent>
                            </Drawer>
                        </NavigationMenuItem>
                    </NavigationMenuList>
                </NavigationMenu>
                {/*!SECTION */}

            </nav >
        </>
    )
}